from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)

    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should tell user to go lower
    outcome, message = check_guess(60, 50)

    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should tell user to go higher
    outcome, message = check_guess(40, 50)

    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"