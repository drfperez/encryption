def calculate_control_letter(dni):
    """
    Calculates the control letter for a Spanish ID number (DNI).
    The input should be a string of 8 digits representing the DNI number.
    Returns the control letter as a string.
    """
    dni = dni.strip().replace('-', '').replace('.', '')
    if not dni.isdigit() or len(dni) != 8:
        raise ValueError('Invalid DNI number')
    control_letter_table = 'TRWAGMYFPDXBNJZSQVHLCKE'
    control_letter_index = int(dni) % 23
    return control_letter_table[control_letter_index]

# Example usage
dni = input('Introduce your Spanish ID number (DNI): ')
control_letter = calculate_control_letter(dni)
print('The control letter for DNI {} is {}'.format(dni, control_letter))
