import subprocess

commands = [
     'curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -',
     'sudo apt-get install -y nodejs',
     'sudo apt-get install -y npm',
     'cd react-test-jenkins/ && npm install',
     'cd react-test-jenkins/ && npm test',
]

for command in commands:
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {command}")
        print(f"Error message: {e}")