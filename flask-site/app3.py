from flask import render_template, request
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from jtoi import complex_to_string


def app3():
    if request.method == 'POST':

        o = complex(request.form['center'].replace('i', 'j'))
        r = float(request.form['radius'])
        a = complex(request.form['a'].replace('i', 'j'))
        b = complex(request.form['b'].replace('i', 'j'))

        plt.figure(figsize=(10, 5))
        plot_circle(o, r, label='Original Circle', color='blue')
        plt.grid(True, linestyle='--', alpha=0.7, which='both', linewidth=0.5)

        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)

        if o != 0:
            new_radius = r * abs(a)
            new_center_shifted = a * o + b
            plot_circle(new_center_shifted, new_radius, label='Final Circle', color='red')

            plt.axis('equal')

            final_circle_center = complex_to_string(new_center_shifted)
            final_circle_radius = str(new_radius)

            img_data = BytesIO()
            plt.savefig(img_data, format='png')
            img_data.seek(0)
            img_base64 = base64.b64encode(img_data.read()).decode('utf-8')
            plt.close()

            return render_template('index3.html', final_circle_center=final_circle_center, o=complex_to_string(o),
                                   a=complex_to_string(a), b=complex_to_string(b), r=r,
                                   final_circle_radius=final_circle_radius, plot=img_base64)

        else:
            new_radius = r * abs(a)
            new_center_shifted = o + b
            plot_circle(new_center_shifted, new_radius, label='Final Circle', color='red')

            plt.axis('equal')

            final_circle_center = complex_to_string(new_center_shifted)
            final_circle_radius = str(new_radius)

            img_data = BytesIO()
            plt.savefig(img_data, format='png')
            img_data.seek(0)
            img_base64 = base64.b64encode(img_data.read()).decode('utf-8')
            plt.close()

            return render_template('index3.html', final_circle_center=final_circle_center,
                                   final_circle_radius=final_circle_radius, plot=img_base64)

    return render_template('index3.html')

def reflection_function(a, b, z):
    return a * z + b

def plot_circle(center, radius, label=None, color='blue'):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = center.real + radius * np.cos(theta)
    y = center.imag + radius * np.sin(theta)
    plt.plot(x, y, label=label, color=color)
    plt.scatter(center.real, center.imag, color=color)


