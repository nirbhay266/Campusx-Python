from main import weather_check

# Test cases fro wether_check function

def test_weather_check():
    assert weather_check(-5) == "It is freezing outside :"
    assert weather_check(10) == "It is a bit chilly!"
    assert weather_check(20) == "The weather is pleasent!"
    assert weather_check(30) ==  "It is hot outside!"

if __name__ == "__main__":
    test_weather_check()