# Password Generator

This project provides a set of functions for generating different types of passwords.

## Features

- Three password generation functions:
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

Here are some examples of how to use the different password generator functions:

```python
# Generate a PIN
pin = PinPasswordGenerator(length=6)
print(f"PIN: {pin}")

# Generate a random password
random_pass = RandomPasswordGenerator(length=12, number=True, symbol=True)
print(f"Random Password: {random_pass}")

# Generate a memorable password
memorable_pass = MemorablePasswordGenerator(number_word=4, separator="-", capital=True)
print(f"Memorable Password: {memorable_pass}")
```

## Function Parameters

### PinPasswordGenerator
- `length` (default: 8): The length of the PIN to generate

### RandomPasswordGenerator
- `length` (default: 8): The length of the password to generate
- `number` (default: False): Include numbers in the password
- `symbol` (default: False): Include symbols in the password

### MemorablePasswordGenerator
- `number_word` (default: 8): The number of words to use in the password
- `separator` (default: '-'): The character used to separate words
- `capital` (default: False): Randomly capitalize words

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

