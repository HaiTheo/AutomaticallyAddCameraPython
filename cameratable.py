from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Load your raw HTML content
with open("camera_raw.html", "r", encoding="utf-8") as file:
    html = file.read()

# Step 2: Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Step 3: Extract rows
rows = soup.select(".table-row")

data = 167

for row in rows:
    cells = row.select(".table-cell")
    # Skip first cell (checkbox), get text from remaining cells
    row_data = [cell.get_text(strip=True) for cell in cells[1:]]
    data.append(row_data)

# Step 4: Set column headers manually
columns = [
    "Device ID", "Name", "IP Address", "Channel", "Port", 
    "Signal", "Status", "Brand", "Note"
]

# Step 5: Convert to DataFrame and export
df = pd.DataFrame(data, columns=columns)
df.to_excel("camera_table.xlsx", index=False)

print("✅ Excel file 'camera_table.xlsx' created successfully!")
