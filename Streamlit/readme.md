# Password Generator

This Streamlit application provides a user-friendly interface for generating various types of passwords.

![Password Generator](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPHE403Xh_ImoW-MmACGAO6ScnVSrdQPdpEw&s)

## Features

The application offers three types of password generators:

1. **Pin Password** : Generates a numeric PIN of specified length.
2. **Random Password** : Creates a random password with options to include numbers and symbols.
3. **Memorable Password** : Generates a password using words, with options for separators and capitalization.

## Usage

1. Select the type of password generator you want to use.
2. Adjust the settings according to your preferences:
   - For Pin and Random passwords: Choose the length
   - For Random passwords: Toggle inclusion of numbers and symbols
   - For Memorable passwords: Choose the number of words, separator, and toggle capitalization
3. The generated password will be displayed instantly.

## Installation

To run this application locally:

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install streamlit
   ```
3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Dependencies

- Streamlit
- Custom Password Generator classes (PinPasswordGenerator, RandomPasswordGenerator, MemorablePasswordGenerator)

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

