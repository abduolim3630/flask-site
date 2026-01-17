from flask import render_template, request
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from jtoi import complex_to_string


def app4():
    if request.method == 'POST':
        try:
            # Read input values from the form
            a = complex(request.form['a'].replace('i', 'j'))
            b = complex(request.form['b'].replace('i', 'j'))
            c = complex(request.form['c'].replace('i', 'j'))
            d = complex(request.form['d'].replace('i', 'j'))
            z = complex(request.form['z'].replace('i', 'j'))

            # Check if ad - bc != 0
            if a * d - b * c == 0:
                raise ValueError("The determinant ad - bc must not be zero.")

            # Apply the fractional linear transformation
            w = fractional_linear_transformation(z, a, b, c, d)

            # Get real and imaginary parts for plotting
            z_real, z_imag = np.real(z), np.imag(z)
            w_real, w_imag = np.real(w), np.imag(w)

            # Create a plot
            plt.figure(figsize=(10, 5))
            plt.grid(True, linestyle='--', alpha=0.5, which='both', linewidth=0.5)

            # Coordinate range
            real_min = min(z_real, w_real, 0) - 1
            real_max = max(z_real, w_real, 0) + 1
            imag_min = min(z_imag, w_imag, 0) - 1
            imag_max = max(z_imag, w_imag, 0) + 1

            # Real and imaginary axes
            plt.plot([real_min, real_max], [0, 0], 'k')
            plt.plot([0, 0], [imag_min, imag_max], 'k')

            # Plotting points for z and w
            plt.scatter(z_real, z_imag, color='blue', s=100, label='z')
            plt.scatter(w_real, w_imag, color='red', s=100, label='w=(a*z+b)/(c*z+d)')

            # Annotate the points
            plt.text(z_real, z_imag, ' z', fontsize=12, color='blue', verticalalignment='bottom',
                     horizontalalignment='right')
            plt.text(w_real, w_imag, ' w', fontsize=12, color='red', verticalalignment='bottom',
                     horizontalalignment='right')

            plt.xlabel('Real Part')
            plt.ylabel('Imaginary Part')
            plt.legend()

            # Save plot to a PNG image and encode it in base64
            img_data = BytesIO()
            plt.savefig(img_data, format='png')
            img_data.seek(0)
            img_base64 = base64.b64encode(img_data.read()).decode('utf-8')
            plt.close()

            # Convert complex numbers from j to i for output
            a_i = complex_to_string(a)
            b_i = complex_to_string(b)
            c_i = complex_to_string(c)
            d_i = complex_to_string(d)
            z_i = complex_to_string(z)
            w_i = complex_to_string(w)

            return render_template('index4.html', a=a_i, b=b_i, c=c_i, d=d_i, z=z_i, w=w_i, plot=img_base64)

        except ValueError as e:
            return render_template('index4.html', error=f"Error: {e}. Please enter valid complex numbers.")
        except Exception as e:
            return render_template('index4.html', error=f"An error occurred: {e}")

    return render_template('index4.html')

def fractional_linear_transformation(z, a, b, c, d):
    return (a * z + b) / (c * z + d)

