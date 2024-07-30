
# Password Generator

This project provides a flexible and extensible password generation system with different types of password generators.

## Features

- Abstract base class `PasswordGenerator` for creating various password generation strategies
- Three concrete implementations:
  - `PinPasswordGenerator`: Generates numeric PINs
  - `RandomPasswordGenerator`: Creates passwords with customizable character sets
  - `MemorablePasswordGenerator`: Produces passwords using real words

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator
   ```

2. Install the required dependencies:
   ```
   pip install nltk
   ```

3. Download the NLTK 'words' corpus:
   ```python
   import nltk
   nltk.download('words')
   ```

## Usage

Here are some examples of how to use the different password generators:

```python
# Generate a PIN
pin_gen = PinPasswordGenerator(length=6)
pin = pin_gen.generate()
print(f"PIN: {pin}")

# Generate a random password
random_gen = RandomPasswordGenerator(length=12, number=True, symbol=True)
random_pass = random_gen.generate()
print(f"Random Password: {random_pass}")

# Generate a memorable password
memorable_gen = MemorablePasswordGenerator(number_word=4, separator="-", capital=True)
memorable_pass = memorable_gen.generate()
print(f"Memorable Password: {memorable_pass}")
```

## Customization

You can easily extend the `PasswordGenerator` base class to create your own password generation strategies.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

