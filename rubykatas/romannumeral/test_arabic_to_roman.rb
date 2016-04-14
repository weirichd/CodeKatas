require 'test/unit'
require 'arabic_to_roman'

class ArabicToRomanTest < Test::Unit::TestCase
    def test_return_MM
    	atr = Arabic_To_Roman.new
      expected = 'MM'
    	actual = atr.return_value 2000
    	assert_equal expected, actual
    end

    def test_return_C
    	atr = Arabic_To_Roman.new
      expected = 'CC'
    	actual = atr.return_value 200
    	assert_equal expected, actual
    end

    def test_return_X
    	atr = Arabic_To_Roman.new
      expected = 'XX'
    	actual = atr.return_value 20
    	assert_equal expected, actual
    end

    def test_return_I
    	atr = Arabic_To_Roman.new
      expected = 'II'
    	actual = atr.return_value 2
    	assert_equal expected, actual
    end

end
