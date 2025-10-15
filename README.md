# Password Strength Analyzer

A Python-based command-line tool to **analyze the strength of passwords** using **entropy calculation**, character diversity checks, and automated **strong password suggestions**.  
It also supports **batch password analysis**, **admin mode**, **history logging**, and **log management**.

----------

##  Features

-    Analyze a single password or a list from a file
    
-    Calculates **bits of entropy** to measure password strength
    
-    Classifies passwords as **Weak**, **Moderate**, **Strong**, or **Very Strong**
    
-    Explains _why_ a password is weak
    
-    **Admin Mode** generates strong random passwords
    
-    Keeps history of all analyzed passwords
    
-    Option to clear the history log
    
-    Beautiful colored terminal output with ASCII banner
    

----------

##  How It Works

The program estimates password strength based on **entropy**:

Entropy=Length×log⁡2(Character Range)Entropy = Length \times \log_2(Character\ Range)Entropy=Length×log2​(Character  Range)

Then it classifies the password:

| Bits of Entropy  | Strength    |
|-------------------|------------|
| < 40              | Weak       |
| 40–70             | Moderate   |
| 70–90             |Strong      |
| > 90              |Very Strong |

If a password is weak, the tool explains the reasons (e.g., missing digits, symbols, uppercase, etc.).

----------

##  Requirements

-   Python 3.8 or higher
    
-   Install dependencies using:
    

`pip install -r requirements.txt` 

### Required Libraries

-   `pyfiglet`
    
-   `colorama`
    

----------

##  Usage

Run the tool from the terminal:

`python3 main.py [options]` 

### Options

| Flag   | Description |
|---------|------------|
| `--password <text>` | Analyze a single password
| `--file <filename>` | Analyze passwords from a file (each line = one password) |
| `--history` | Show previously analyzed passwords |
| `--admin` | Generate strong random passwords (admin mode)|
| `--clear`| Clear the password history log |
| `-h`, `--help` | Show help message |

----------

##  Examples

### Analyze a single password:

`python3 main.py --password "F@thy2025!"` 

### Analyze multiple passwords from a file:

`python3 main.py --file passwords.txt` 

### Run admin mode (generate 3 strong passwords):

`python3 main.py --admin` 

### View password analysis history:

`python3 main.py --history` 

### Clear the history log:

`python3 main.py --clear` 

----------

## Log File

All password analysis results are stored in a file named **`log`** in the project directory.  
Each entry includes:

`Password:  ********  |  Entropy:  78.45  |  Strength:  Strong  |  at  time  2025-10-10 11:30:21` 


