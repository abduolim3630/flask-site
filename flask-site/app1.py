from flask import render_template, request
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from jtoi import complex_to_string


def app1():
    if request.method == 'POST':
        try:
            a = complex(request.form['a'].replace('i', 'j'))
            b = complex(request.form['b'].replace('i', 'j'))
            z = complex(request.form['z'].replace('i', 'j'))
            w = reflection_function(a, b, z)
#           n = calculate_result(z, w)

            # Grafik
            z_real, z_imag = np.real(z), np.imag(z)
            w_real, w_imag = np.real(w), np.imag(w)

            # chizma yaratish
            plt.figure(figsize=(10, 5))
            plt.grid(True, linestyle='--', alpha=0.5, which='both', linewidth=0.5)

            # koordinata o'lchami
            real_min = min(z_real, w_real, 0) - 1
            real_max = max(z_real, w_real, 0) + 1
            imag_min = min(z_imag, w_imag, 0) - 1
            imag_max = max(z_imag, w_imag, 0) + 1

            # haqiqiy va mavhum o'qlar
            plt.plot([real_min, real_max], [0, 0], 'k')
            plt.plot([0, 0], [imag_min, imag_max], 'k')

            # Grafik o'lchamini avtomatik qilish
            plt.xlim([real_min, real_max])
            plt.ylim([imag_min, imag_max])

            plt.quiver(0, 0, z_real, z_imag, angles='xy', scale_units='xy', scale=1, color='blue', label='z')
            plt.quiver(0, 0, w_real, w_imag, angles='xy', scale_units='xy', scale=1, color='red', label='w=a•z+b')

            plt.xlabel('Im(z)')
            plt.ylabel('Re(z)')
            plt.legend()

            img_data = BytesIO()
            plt.savefig(img_data, format='png')
            img_data.seek(0)
            img_base64 = base64.b64encode(img_data.read()).decode('utf-8')
            plt.close()

            # Convert complex numbers from j to i for output
            a_i = complex_to_string(a)
            b_i = complex_to_string(b)
            z_i = complex_to_string(z)
            w_i = complex_to_string(w)

            return render_template('index1.html', a=a_i, b=b_i, z=z_i, w=w_i, plot=img_base64)

        except ValueError as e:
            return render_template('index1.html', error=f"Error: {e}. Please enter valid complex numbers.")
        except Exception as e:
            return render_template('index1.html', error=f"An error occurred: {e}")

    return render_template('index1.html')

def reflection_function(a, b, z):
    return a * z + b
