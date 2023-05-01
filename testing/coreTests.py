from core.session import Sessions, UserSession
from database.db import Database
from core.utils import calculate_total_cost




def test_init_sessions() -> tuple:
    """
    Tests that the Sessions class is initialized correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    sessions = Sessions()

    if len(sessions.sessions) != 0:
        error = f"Error in test_init_sessions: Sessions dictionary is not empty.\n  - Actual: {len(sessions.sessions)}"
        return False, error
    else:
        return True, "Sessions dictionary is empty."


def test_add_new_session() -> tuple:
    """
    Tests that a new session is added correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/storeRecords.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)

    if len(sessions.sessions) == 0:
        error = f"Error in test_add_new_session: Sessions dictionary is empty.\n  - Actual: {len(sessions.sessions)}"
        return False, error
    else:
        return True, "Sessions dictionary is not empty."
    
# Tests logout function - MSR
def test_remove_session() -> tuple:
    """
    Tests that a session is removed correctly.

    args:
        - None

    return: 
        - a tuple is returned containing a boolean and a string, 
          where boolean is True if the test passed and False if the test failed.
          The String in the tuple gives a error report if the test failed.
    """
    db = Database("database/storeRecords.db")
    sessions = Sessions()
    sessions.remove_session("test")

    if len(sessions.sessions) == 0:
        success = "removed session successfully"
        return True, success
    else:
        error = f"Error in test_remove_session: Sessions dictionary is note empty.\n  - Actual: {len(sessions.sessions)}"
        return False, error


def test_get_session() -> tuple:
    """
    Tests that a session is retrieved correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/storeRecords.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)
    session = sessions.get_session("test")

    if not isinstance(session, UserSession):
        error = f"Error in test_get_session: Session is not a UserSession object.\n  - Actual: {type(session)}"
        return False, error
    else:
        return True, "Session is a UserSession object."


def test_get_session_username() -> tuple:
    """
    Tests that a session's username is retrieved correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/storeRecords.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)
    session = sessions.get_session("test")

    if session.username != "test":
        error = f"Error in test_get_session_username: Session's username is incorrect.\n  - Expected: test\n  - Actual: {session.username}"
        return False, error
    else:
        return True, "Session's username is correct."


def test_get_session_db() -> tuple:
    """
    Tests that a session's database is retrieved correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/storeRecords.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)
    session = sessions.get_session("test")

    if session.db != db:
        error = f"Error in test_get_session_db: Session's database is incorrect.\n  - Expected: {db}\n  - Actual: {session.db}"
        return False, error
    else:
        return True, "Session's database is correct."

def test_calculate_total_cost() -> tuple:
    items = {
        'name': 'lizard',
        'price': 2.0,
        'quantity': 0,
        'discount': 0,
        'tax_rate': 0
    }
    num = calculate_total_cost(items)

    if num != 2:
        error = f"Error in test_calculate_total_cost: incorrect totals\n  - Expected: 2\n  - Actual: {num}"
        return False, error
    else:
        return True, "calculation is correct."
    

