require 'test/unit'
require 'arabic_to_roman'

class ArabicToRomanTest < Test::Unit::TestCase
    def test_return_I_if_given_one
    	atr = Arabic_To_Roman.new
    	expected = atr.return_value 1
    	assert_equal expected, 'I'
    end

    def test_return_III_if_given_three
    	atr = Arabic_To_Roman.new
    	expected = atr.return_value 3
    	assert_equal expected, 'III'
    end
end
