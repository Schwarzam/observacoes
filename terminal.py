import subprocess

def run_command(command, timeout=None):
    """
    Executes a shell command with an optional timeout and returns its output and exit code.

    Parameters:
        command (str or list): The shell command to execute. Can be a string or a list of arguments.
        timeout (int, optional): The maximum time in seconds to wait for the command to complete.

    Returns:
        tuple: (output, exit_code)
               - output (str): The captured standard output and error combined.
               - exit_code (int): The exit code of the command.
    """
    try:
        # Run the command with a timeout
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,  # Capture standard output
            stderr=subprocess.STDOUT,  # Capture standard error along with stdout
            text=True,  # Decode output as text (string)
            shell=isinstance(command, str),  # Use shell if command is a string
            timeout=timeout  # Timeout in seconds
        )
        return result.stdout, result.returncode
    except subprocess.TimeoutExpired as e:
        # Handle timeout scenario
        return f"Error: Command timed out after {timeout} seconds", -1
    except Exception as e:
        # Handle other exceptions
        return f"Error: {str(e)}", -1