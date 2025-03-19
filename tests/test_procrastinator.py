import pytest
from src.code_procrastinator.procrastinator import excuse_wrapper, EXCUSE_INIT_MESSAGE, EXCUSE_MESSAGE, EXCUSE_END_MESSAGE
import logging
logger = logging.getLogger(__name__)

# First test group: a simple hello world test.
class Tests:
    def test_hello_world(self):
        string = "Hello World"
        assert string == "Hello World"

# Second test group: tests for the reaffirm_program function.
from src.code_procrastinator.procrastinator import reaffirm_program, procrastinate, time, POSITIVE_RESPONSES, DEFAULT_RESPONSES, random_fail_wrapper, IllDoItLaterException, random_procrastinate

def test_reaffirm_program_with_positive_input(capsys):
    # Provide a message containing at least one positive keyword.
    positive_message = "I think you're doing an awesome job!"
    result = reaffirm_program(positive_message)
    
    captured = capsys.readouterr().out.strip()
    
    # The output should be one of the positive responses.
    assert captured in POSITIVE_RESPONSES, "The positive response was not printed as expected."
    
    # The function should return the running message.
    assert result == "Program is now running! Let's do this!"

def test_reaffirm_program_with_negative_input(capsys):
    # Provide a message that doesn't contain any positive keywords.
    negative_message = "I don't really care about this."
    result = reaffirm_program(negative_message)
    
    captured = capsys.readouterr().out.strip()
    
    # The output should be one of the default responses.
    assert captured in DEFAULT_RESPONSES, "The default response was not printed as expected."
    
    # None since the decorator skips execution.
    assert result is None



# Tests for procrasintaor 
@pytest.fixture
def mock_sleep(monkeypatch):
    # Do nothing, preventing actual sleep
    def fake_sleep(_):
        pass
    monkeypatch.setattr(time, "sleep", fake_sleep)

def test_procrastinator(mock_sleep, capsys):
    # Provide a positive integer for the max time per delay and amount of delays
    seconds = 10
    delay_count = 3

    delays = procrastinate(seconds, delay_count)

    # The output should include 3 console responses each taking 10 seconds or less to print
    assert len(delays) == delay_count
    assert all(0 <= d <= seconds for d in delays)

    captured = capsys.readouterr()
    output_lines = captured.out.strip().split("\n")

    # Check if the correct number of lines were printed
    assert len(output_lines) == delay_count
    assert all("Procrastinating for" in line for line in output_lines)

def test_excuse_function_outputs(capsys):
    @excuse_wrapper
    def add(x, y):
        return x + y
    
    add(1, 2)
    output = capsys.readouterr().out.strip().split("\n")
    # First response expected
    assert output[0] in EXCUSE_INIT_MESSAGE
    
    # Second response expected
    assert output[3] in EXCUSE_MESSAGE
    
    # Last response expected
    assert output[4] in EXCUSE_END_MESSAGE

def test_random_fail_wrapper_executes():
    """Test that random_run executes the function when it does not raise an exception."""
    @random_fail_wrapper
    def test_func():
        return "Function executed!"

    # Run multiple times to account for randomness
    for _ in range(10):
        try:
            result = test_func()
            assert result == "Function executed!"
        except IllDoItLaterException:
            pass  # It's okay if it fails, since it's expected sometimes

def test_random_fail_wrapper_raises_exception():
    """Test that random_run sometimes raises IllDoItLaterException."""
    @random_fail_wrapper
    def test_func():
        return "Function executed!"

    raised = False
    for _ in range(10):  # Run multiple times to increase the chance of failure
        try:
            test_func()
        except IllDoItLaterException:
            raised = True
            break

    assert raised, "random_run should sometimes raise IllDoItLaterException"

def test_random_procrastinate_applies_a_wrapper():
    """Test that random_wrapper applies one of the decorators and modifies function behavior."""
    @random_procrastinate
    def test_func():
        return "Function executed!"

    # Try calling it and make sure it behaves in a decorated way
    try:
        result = test_func("You're amazing!")  # In case require_positive_input is selected
        assert result is None or result == "Function executed!"
    except IllDoItLaterException:
        pass  # Expected if random_fail_wrapper was chosen

def test_random_procrastinate_changes_behavior():
    """Test that random_wrapper randomly applies different wrappers."""
    applied_wrappers = set()

    for _ in range(10):  # Run multiple times to observe different behaviors
        @random_procrastinate
        def test_func():
            return "Function executed!"

        try:
            result = test_func("You're amazing!")
            if result == "Function executed!":
                applied_wrappers.add("ran_successfully")
            elif result is None:
                applied_wrappers.add("required_positive_input")
        except IllDoItLaterException:
            applied_wrappers.add("ill_do_it_later")

    # Ensure that at least two different behaviors were observed
    assert len(applied_wrappers) >= 2, "random_wrapper should apply different behaviors randomly"