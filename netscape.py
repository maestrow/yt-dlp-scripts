# https://stackoverflow.com/a/70947982/1189832

# For anyone that wants all of the cookies for a site, but doesn't want to use an extension:

# Open developer tools -> Application -> Cookies.
# Select the first cookie in the list and hit Ctrl/Cmd-A
# Copy all of the data in this table with Ctrl/Cmd-C
# Now you have a TSV (tab-separated value) string of cookie data. You can process this in any language you want, but in Python (for example):

import io
import pandas as pd
import numpy as np

def read_cookies():
    # Read content from text file:
    with open('cookies-chrome.txt', 'r') as f:
        cookie_str = f.read().strip()
    return cookie_str
    

cookie_str = read_cookies()

# Copied from the developer tools window.
cols = ['name', 'value', 'domain', 'path', 'max_age', 'size', 'http_only', 'secure', 'same_party', 'priority']

# Parse into a dataframe.
df = pd.read_csv(io.StringIO(cookie_str), sep='\t', names=cols, index_col=False)

# Now you can export them in Netscape format:

# Fill in NaNs and format True/False for cookies.txt.
df = df.fillna(False).assign(flag=True).replace({True: 'TRUE', False: 'FALSE'})
# Get unix timestamp from max_age
max_age = (
    df.max_age
    .replace({'Session': np.nan})
    .pipe(pd.to_datetime))
start = pd.Timestamp("1970-01-01", tz='UTC')
max_age = (
    ((max_age - start) // pd.Timedelta('1s'))
    .fillna(0)  # Session expiry are 0s
    .astype(int))  # Floats end with ".0"
df = df.assign(max_age=max_age)

cookie_file_cols = ['domain', 'flag', 'path', 'secure', 'max_age', 'name', 'value']
with open('cookies.txt', 'w') as fh:
  # Python's cookiejar wants this header.
  fh.write('# Netscape HTTP Cookie File\n')
  df[cookie_file_cols].to_csv(fh, sep='\t', index=False, header=False)


# And finally, back to the shell:

# # Get user agent from navigator.userAgent in devtools
# wget -U $USER_AGENT --load-cookies cookies.txt $YOUR_URL