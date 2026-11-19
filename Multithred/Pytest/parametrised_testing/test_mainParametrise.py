from main import weather_check
import pytest

# Test cases fro wether_check function

# def test_weather_check():
#     assert weather_check(-5) == "It is freezing outside :"
#     assert weather_check(10) == "It is a bit chilly!"
#     assert weather_check(20) == "The weather is pleasent!"
#     assert weather_check(30) ==  "It is hot outside!"

@pytest.mark.parametrize("temp,expected",[
    (-5,"It's freezing outside!"),
    (10,"It's a bit chilly."),
    (20,"The weather is pleasant." ),
    (30, "It's hot outside!")
])

def test_weather_check(temp,expected):
    assert weather_check(temp) == expected

if __name__ == "__main__":
    test_weather_check()


