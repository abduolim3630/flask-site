from flask import render_template, request
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from jtoi import complex_to_string

def app2():
    if request.method == 'POST':
        try:
            a = complex(request.form['a'].replace('i', 'j'))
            b = complex(request.form['b'].replace('i', 'j'))

            n = int(request.form['n'])
            if n < 2:
                raise ValueError("Nuqtalar sonini kamida 2 ta kiriting")

            polygon_points = []
            reflected_points = []

            for i in range(1, n + 1):
                z_str = request.form[f'z{i}'].replace('i', 'j')
                z = complex(z_str)
                polygon_points.append(z)
                reflected = reflection_function(z, a, b)
                reflected_points.append(reflected)

            plt.figure(figsize=(10, 5))

            real_min = min(np.real(polygon_points + reflected_points) + [0]) - 1
            real_max = max(np.real(polygon_points + reflected_points) + [0]) + 1
            imag_min = min(np.imag(polygon_points + reflected_points) + [0]) - 1
            imag_max = max(np.imag(polygon_points + reflected_points) + [0]) + 1

            plt.axhline(0, color='black', linewidth=1)
            plt.axvline(0, color='black', linewidth=1)

            plt.xlim([real_min, real_max])
            plt.ylim([imag_min, imag_max])

            plt.scatter(np.real(polygon_points), np.imag(polygon_points), label="Original Point", marker='o',
                        color='b')
            plt.scatter(np.real(reflected_points), np.imag(reflected_points), label="Final Point",
                        marker='x', color='r')

            polygon_points.append(polygon_points[0])
            reflected_points.append(reflected_points[0])
            plt.plot(np.real(polygon_points), np.imag(polygon_points), 'b--')
            plt.plot(np.real(reflected_points), np.imag(reflected_points), 'r--')

            plt.xlabel('Real')
            plt.ylabel('Imaginary')
            plt.legend()
            if n == 2:
                plt.title("")
            else:
                plt.title(f'')
            plt.grid(True)

            # Save the plot to a BytesIO object
            img_data = BytesIO()
            plt.savefig(img_data, format='png')
            img_data.seek(0)
            img_base64 = base64.b64encode(img_data.read()).decode('utf-8')
            plt.close()

            polygon_points_i = [complex_to_string(z) for z in polygon_points[:-1]]
            reflected_points_i = [complex_to_string(w) for w in reflected_points[:-1]]

            a_i = complex_to_string(a)
            b_i = complex_to_string(b)

            return render_template('index2.html', plot=img_base64, reflected_points=reflected_points_i,
                                   polygon_points=polygon_points_i, a=a_i, b=b_i)

        except ValueError as e:
            return render_template('index2.html', error=f"Error: {e}. Nuqtalar sonini kamida 2 ta kiriting ")
        except Exception as e:
            return render_template('index2.html', error=f"Xatolik yuz berdi: {e}")

    return render_template('index2.html')

def reflection_function(a, b, z):
    return a * z + b

