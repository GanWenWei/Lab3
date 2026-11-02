import lab2.lab2 as bmi_value


def test_bmi_normal_weight():
    bmi,classification = bmi_value.calculate_bmi(1.75, 70)
    assert classification == 0
    


def test_bmi_over_weight():
    bmi,classification = bmi_value.calculate_bmi(1.70, 90)
    assert classification == 1

def test_bmi_under_weight():
    bmi,classification = bmi_value.calculate_bmi(1.70, 45)
    assert classification == -1