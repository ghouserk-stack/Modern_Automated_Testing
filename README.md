**Assignment1**

Ghouser Kaleel Mohamed Ismail

Student ID: 9072814

Date: 28/09/2025

# Unit Test Suite for Password Meter

## Source Code Suitable for Unit Testing

The unit test is used to test the individual components or unit that
performs some specific set of tasks. Here the following methods with
parameter are an individual unit to perform unit testing with preset
values.

Hence the following methods are the part of the source code suitable for
unit testing.

Git Link:
<https://github.com/Mrinank-Bhowmick/python-beginner-projects/tree/main/projects/Password%20Projects/Password%20Meter>

def numberOfCharacters(password):

    bonus = len(password) \* 4

    return bonus

def upperCaseLetters(password):

    charsUpper = 0

    if not password.isupper():

        for i in password:

            if i.isupper():

                charsUpper += 1

        if charsUpper != 0:

            charsUpper = (len(password) - charsUpper) \* 2

    return charsUpper

def lowerCaseLetters(password):

    charsLower = 0

    if password.islower():

        for i in password:

            if i.islower() and i not in acentos:

                charsLower += 1

        if charsLower != 0:

            charsLower = (len(password) - charsLower) \* 2

    return charsLower

def numbers(password):

    charsNumber = 0

    if not password.isdigit():

        for i in password:

            if i.isdigit():

                charsNumber += 1

    return charsNumber \* 4

def symbols(password):

    charsSymbol = 0

    for i in password:

        if (

            i.lower() not in sequenceAlphabet

            and i not in exceptions

            and i not in sequenceNumbers

        ):

            charsSymbol += 1

    return charsSymbol \* 6

def middleNumberOrSymbol(password):

    CharsMiddle = 0

    for i in range(1, len(password)):

        if (

            password\[i\].isdigit()

            or (

                password\[i\].lower() not in sequenceAlphabet

                and password\[i\] not in exceptions

            )

        ) and i != len(password) - 1:

            CharsMiddle += 1

    return CharsMiddle \* 2

def requirements(password):

    requirementsCount = 0

    if len(password) \>= 8:

        requirementsCount += 1

        if upperCaseLetters(password) \> 0:

            requirementsCount += 1

        if lowerCaseLetters(password) \> 0:

            requirementsCount += 1

        if numbers(password) \> 0:

            requirementsCount += 1

        if symbols(password) \> 0:

            requirementsCount += 1

        if requirementsCount == 4:

            requirementsCount = requirementsCount \* 2

        else:

            requirementsCount = 0

    return requirementsCount

def lettersOnly(password):

    countDigit = 0

    for i in password:

        if i.isdigit():

            countDigit += 1

    if countDigit == 0:

        countDigit = len(password) \* -1

    else:

        countDigit = 0

    return countDigit

def numbersOnly(password):

    countLetters = 0

    for i in password:

        if i.isalpha():

            countLetters += 1

    if countLetters == 0:

        return len(password) \* -1

    else:

        countLetters = 0

    return countLetters

def consecutiveLowerCase(password):

    countLowerCase = 0

    password = password + "1"

    for i in range(len(password)):

        if (

            password\[i\].islower()

            and password\[i + 1\].islower()

            and password\[i + 1\] not in acentos

            and password\[i\] not in acentos

        ):

            countLowerCase += 1

    return (countLowerCase \* 2) \* -1

def consecutiveUpperCase(password):

    countUpperCase = 0

    password = password + "1"

    for i in range(len(password)):

        if password\[i\].isupper() and password\[i + 1\].isupper():

            countUpperCase += 1

    return (countUpperCase \* 2) \* -1

def consecutiveNumbers(password):

    countNumbers = 0

    password = password + "a"

    for i in range(len(password)):

        if password\[i\].isdigit() and password\[i + 1\].isdigit():

            countNumbers += 1

    return (countNumbers \* 2) \* -1

def sequentialNumbers(password):

    numbers = ""

    countNumbers = 0

    for i in range(len(password)):

        numbers += password\[i : i + 3\]

        if numbers in sequenceNumbers and len(numbers) == 3:

            countNumbers += 1

        numbers = ""

    return (countNumbers \* 3) \* -1

def sequentialLetters(password):

    letters = ""

    countLetters = 0

    for i in range(len(password)):

        letters += password\[i : i + 3\]

        if letters in sequenceAlphabet and len(letters) == 3:

            countLetters += 1

        letters = ""

    return (countLetters \* 3) \* -1

## Unit Testing Component Coverage and Flowchart

.

The following component needs to be covered with unit testing for
password meter.

- Number of Characters

  - Verify length of the password (length\*4)

- Uppercase letters

<!-- -->

- Verify the password has uppercase letters and gives the positive score
  of upper-case letters.

<!-- -->

- Lowercase letters

  - Verify the password has lowercase letters and gives the positive
    score of lower-case letters.

- Numbers

  - Verify the password has numbers and gives the positive score of
    numbers.

- Symbols

  - Verify the password has symbols and gives the positive score of
    symbols.

- Middle Number or Symbol

  - Verify the password has middle number or symbol and gives the
    positive score of middle number or symbol.

- Requirements

  - Verify the password has requirements full filled and increases the
    score of passwords.

- Letters Only

  - Verify the password has only letters and gives the negative score of
    letters only.

- Numbers Only

  - Verify the password has only numbers and gives the negative score of
    numbers only.

- Consecutive Lower case

  - Verify the password has consecutive lower case and gives the
    negative score of consecutive lower case.

- Consecutive Upper case

  - Verify the password has consecutive upper case and gives the
    negative score of consecutive upper case.

- Consecutive Numbers

  - Verify the password has consecutive numbers and gives the negative
    score of consecutive numbers.

- Sequential Numbers

  - Verify the password has sequential numbers and gives the negative
    score of sequential numbers.

- Sequential Letters

  - Verify the password has sequential letters and gives the negative
    score of

  - Sequential letters.

Flowchart- Unit Testing

Start

Unit Test -Pass

Password=”AcZFdn\$5”

Check every methods Results (eg. Method: Number of Character; expected
value= 32)

Unit Test -Fail

No

End

## Test Classes

### Regular Test case:

This test case is used to check whether the code works for standard
conditions like actual results are obtained for exactly given inputs.

In this program, various components are checked as mentioned in the
section 2. eg: Number of characters, Uppercase letters …

I have created test classes to check the number of characters against
expected results.

Eg Password: “AcZFdn\$5”

Expected Results=32 Actual Results = 32

Test Passed

### Edge Test case:

This test case is used to test the extreme values (minimum and maximum
values), boundary conditions, and unusual cases or unexpected behaviour.

In this program, we cannot do the edge case scenario as it will always
produce the score irrespective of the password.

However, I did negative test by assigning the expected value as
different than actual value as explained.

Eg Password: AcZFdn\$5

Expected Results=30 Actual Results = 32

Test Failed

## Unit Tests

As this program contains several methods, I have created the unit test
for two of the methods. It is possible to create unit tests for all
other methods.

Unit Test Code is mentioned below

import unittest

import meter_pass

\# from meter_pass import numberOfCharacters

class Testleng(unittest.TestCase):

def test_len(self):

expected_value = 32

actual_method = meter_pass.numberOfCharacters("AcZFdn\$5")

self.assertEqual(actual_method, expected_value)

def test_not_matched_len(self):

expected_value = 30

actual_method = meter_pass.numberOfCharacters("AcZFdn\$5")

self.assertEqual(expected_value, actual_method)

def test_upper(self):

expected_value = 8

actual_method = meter_pass.upperCaseLetters("Arcom")

self.assertEqual(actual_method, expected_value)

def test_not_upper(self):

expected_value = 15

actual_method = meter_pass.upperCaseLetters("Arcom")

self.assertEqual(expected_value, actual_method)

if \_\_name\_\_== "\_\_main\_\_":

unittest.main()

### 

### 
