from django.test import TestCase

from backend.src import translate


class translateTestCase(TestCase):
    def test_translate_one_digit(self):
        self.assertEqual(translate("1"), "one")
        self.assertEqual(translate("2"), "two")
        self.assertEqual(translate("0"), "zero")

    def test_translate_two_digits(self):
        self.assertEqual(translate("11"), "eleven")
        self.assertEqual(translate("21"), "twenty one")
        self.assertEqual(translate("25"), "twenty five")
        self.assertEqual(translate("33"), "thirty three")
        self.assertEqual(translate("99"), "ninety nine")
        self.assertEqual(translate("00"), "zero")
        self.assertEqual(translate("01"), "one")

    def test_translate_three_digits(self):
        self.assertEqual(translate("123"), "one hundred twenty three")
        self.assertEqual(translate("586"), "five hundred eighty six")
        self.assertEqual(translate("000"), "zero")
        self.assertEqual(translate("001"), "one")

    def test_translate_four_digits(self):
        self.assertEqual(translate("9834"), "nine thousand eight hundred thirty four")
        self.assertEqual(translate("0000"), "zero")
        self.assertEqual(translate("0001"), "one")

    def test_translate_five_digits(self):
        self.assertEqual(
            translate("56423"), "fifty six thousand four hundred twenty three"
        )
        self.assertEqual(translate("00000"), "zero")

    def test_translate_six_digits(self):
        self.assertEqual(
            translate("682675"),
            "six hundred eighty two thousand six hundred seventy five",
        )

    def test_transalte_seven_digits(self):
        self.assertEqual(
            translate("2964982"),
            "two million nine hundred sixty four thousand nine hundred eighty two",
        )

    def test_translate_eight_digits(self):
        self.assertEqual(
            translate("27852509"),
            "twenty seven million eight hundred fifty two thousand five hundred nine",
        )
        self.assertEqual(
            translate("12345678"),
            "twelve million three hundred forty five thousand six hundred seventy eight",
        )

    def test_translate_nine_digits(self):
        self.assertEqual(
            translate("123456789"),
            "one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine",
        )

    def test_translate_ten_digits(self):
        self.assertEqual(
            translate("1234567893"),
            "one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety three",
        )

    def test_tranlate_edge_cases(self):
        with self.assertRaises(ValueError):
            translate("-1")

        with self.assertRaises(ValueError):
            translate("0.1")

        with self.assertRaises(ValueError):
            translate("a1")

        with self.assertRaises(ValueError):
            translate("")
