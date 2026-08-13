import pytest
from validators import is_valid_email


class TestEmailValidationNormalCases:
    """Test cases for valid email addresses."""

    def test_simple_email(self):
        """Test basic valid email format."""
        assert is_valid_email("user@example.com") is True

    def test_email_with_numbers(self):
        """Test email with numbers."""
        assert is_valid_email("user123@example123.com") is True

    def test_email_with_dot_in_local_part(self):
        """Test email with dot in the local part."""
        assert is_valid_email("user.name@example.com") is True

    def test_email_with_plus_in_local_part(self):
        """Test email with plus sign (common for filtering)."""
        assert is_valid_email("user+tag@example.com") is True

    def test_email_with_hyphen_in_domain(self):
        """Test email with hyphen in domain."""
        assert is_valid_email("user@example-domain.com") is True

    def test_email_with_underscore_in_local_part(self):
        """Test email with underscore."""
        assert is_valid_email("user_name@example.com") is True

    def test_email_with_percent_in_local_part(self):
        """Test email with percent sign."""
        assert is_valid_email("user%test@example.com") is True

    def test_email_with_uppercase(self):
        """Test email with uppercase letters."""
        assert is_valid_email("User@Example.COM") is True

    def test_email_with_mixed_case(self):
        """Test email with mixed case."""
        assert is_valid_email("UserName@ExampleDomain.Com") is True

    def test_email_with_subdomain(self):
        """Test email with subdomain."""
        assert is_valid_email("user@mail.example.com") is True

    def test_email_with_multiple_subdomains(self):
        """Test email with multiple subdomains."""
        assert is_valid_email("user@mail.support.example.com") is True

    def test_email_single_char_local_part(self):
        """Test email with single character local part."""
        assert is_valid_email("a@example.com") is True

    def test_email_with_two_letter_tld(self):
        """Test email with two-letter top-level domain."""
        assert is_valid_email("user@example.co") is True

    def test_email_with_long_tld(self):
        """Test email with longer top-level domain."""
        assert is_valid_email("user@example.museum") is True


class TestEmailValidationBoundaryCases:
    """Test cases for boundary conditions."""

    def test_email_with_single_char_domain(self):
        """Test email with single character in domain name."""
        assert is_valid_email("user@a.com") is True

    def test_email_with_long_local_part(self):
        """Test email with very long local part."""
        long_local = "a" * 64 + "@example.com"
        assert is_valid_email(long_local) is True

    def test_email_with_long_domain(self):
        """Test email with very long domain."""
        long_domain = "user@" + "a" * 63 + ".com"
        assert is_valid_email(long_domain) is True

    def test_email_with_multiple_dots_in_local(self):
        """Test email with consecutive dots in local part."""
        assert is_valid_email("user.name.test@example.com") is True

    def test_email_with_dot_before_at(self):
        """Test email ending with dot before @ (valid in pattern)."""
        assert is_valid_email("user.@example.com") is True

    def test_email_starting_with_special_char(self):
        """Test email starting with special character."""
        assert is_valid_email("+user@example.com") is True

    def test_numeric_tld_minimum(self):
        """Test with exactly 2-letter TLD (minimum boundary)."""
        assert is_valid_email("user@example.co") is True


class TestEmailValidationNegativeCases:
    """Test cases for invalid email addresses."""

    def test_empty_string(self):
        """Test empty string."""
        assert is_valid_email("") is False

    def test_no_at_symbol(self):
        """Test email without @ symbol."""
        assert is_valid_email("userexample.com") is False

    def test_multiple_at_symbols(self):
        """Test email with multiple @ symbols."""
        assert is_valid_email("user@example@com") is False

    def test_no_domain(self):
        """Test email without domain."""
        assert is_valid_email("user@") is False

    def test_no_local_part(self):
        """Test email without local part."""
        assert is_valid_email("@example.com") is False

    def test_no_tld(self):
        """Test email without top-level domain."""
        assert is_valid_email("user@example") is False

    def test_tld_too_short(self):
        """Test with TLD having less than 2 letters."""
        assert is_valid_email("user@example.c") is False

    def test_only_at_symbol(self):
        """Test with only @ symbol."""
        assert is_valid_email("@") is False

    def test_space_in_email(self):
        """Test email with space."""
        assert is_valid_email("user name@example.com") is False

    def test_space_in_domain(self):
        """Test email with space in domain."""
        assert is_valid_email("user@example domain.com") is False

    def test_comma_in_local_part(self):
        """Test email with comma (not allowed)."""
        assert is_valid_email("user,name@example.com") is False

    def test_invalid_special_char_in_local(self):
        """Test email with invalid special character."""
        assert is_valid_email("user!name@example.com") is False

    def test_invalid_special_char_in_domain(self):
        """Test email with invalid character in domain."""
        assert is_valid_email("user@exam!ple.com") is False

    def test_domain_starts_with_hyphen(self):
        """Test domain starting with hyphen."""
        assert is_valid_email("user@-example.com") is False

    def test_domain_ends_with_hyphen(self):
        """Test domain ending with hyphen."""
        assert is_valid_email("user@example-.com") is False

    def test_tld_has_numbers(self):
        """Test TLD with numbers (invalid)."""
        assert is_valid_email("user@example.c0m") is False

    def test_tld_has_hyphen(self):
        """Test TLD with hyphen (invalid)."""
        assert is_valid_email("user@example.co-m") is False

    def test_consecutive_dots_in_domain(self):
        """Test domain with consecutive dots."""
        assert is_valid_email("user@example..com") is False

    def test_dot_before_at(self):
        """Test dot directly before @."""
        # This is technically allowed by the pattern, but commenting for awareness
        assert is_valid_email(".user@example.com") is False


class TestEmailValidationEdgeCases:
    """Test cases for edge cases and special scenarios."""

    def test_none_input(self):
        """Test with None input."""
        assert is_valid_email(None) is False

    def test_integer_input(self):
        """Test with integer input."""
        assert is_valid_email(123) is False

    def test_float_input(self):
        """Test with float input."""
        assert is_valid_email(123.456) is False

    def test_list_input(self):
        """Test with list input."""
        assert is_valid_email([]) is False

    def test_dict_input(self):
        """Test with dictionary input."""
        assert is_valid_email({}) is False

    def test_boolean_input(self):
        """Test with boolean input."""
        assert is_valid_email(True) is False
        assert is_valid_email(False) is False

    def test_unicode_characters(self):
        """Test with unicode characters."""
        assert is_valid_email("üser@example.com") is False

    def test_emoji_in_email(self):
        """Test with emoji characters."""
        assert is_valid_email("user😀@example.com") is False

    def test_newline_in_email(self):
        """Test with newline character."""
        assert is_valid_email("user\n@example.com") is False

    def test_tab_in_email(self):
        """Test with tab character."""
        assert is_valid_email("user\t@example.com") is False

    def test_at_only(self):
        """Test with only @ symbol."""
        assert is_valid_email("@") is False

    def test_very_long_email(self):
        """Test with extremely long email address."""
        long_email = "a" * 200 + "@" + "b" * 200 + ".com"
        assert is_valid_email(long_email) is True

    def test_numeric_local_part(self):
        """Test with numeric-only local part."""
        assert is_valid_email("12345@example.com") is True

    def test_numeric_domain(self):
        """Test with numeric domain (should be valid per pattern)."""
        assert is_valid_email("user@123.com") is True

    def test_hyphen_in_subdomain(self):
        """Test hyphen in subdomain part."""
        assert is_valid_email("user@mail-server.example.com") is True

    def test_trailing_dot(self):
        """Test email with trailing dot."""
        assert is_valid_email("user@example.com.") is False

    def test_leading_dot_in_local(self):
        """Test local part starting with dot."""
        assert is_valid_email(".user@example.com") is False

    def test_multiple_consecutive_special_chars(self):
        """Test with multiple consecutive special characters."""
        assert is_valid_email("user++tag@example.com") is True
        assert is_valid_email("user__name@example.com") is True
        assert is_valid_email("user%%test@example.com") is True

    def test_dash_in_local_part(self):
        """Test if dash is allowed in local part (not in pattern)."""
        assert is_valid_email("user-name@example.com") is False
