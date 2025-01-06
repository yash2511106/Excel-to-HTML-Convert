import pandas as pd

def excel_to_html(file_path, output_html):
    
        
        df = pd.read_excel(file_path)

        
        html_table = df.to_html(index=False, border=1, justify='center', classes='styled-table')  

            
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Excel to HTML Table</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                .styled-table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                .styled-table th, .styled-table td {{
                    border: 1px solid #dddddd;
                    text-align: center;
                    padding: 8px;
                }}
                .styled-table th {{
                    background-color: #f2f2f2;
                }}
            </style>
        </head>
        <body>
            <h2>Generated HTML Table</h2>
            {html_table}
        </body>
        </html>
        """


        with open(output_html, "w", encoding="utf-8") as f:
            f.write(html_content)   # create and save the html content in output_html file

        print(f"HTML table generated successfully! Saved to {output_html}")
   


excel_file = "path of excel file"  
output_file = "output_table.html"
excel_to_html(excel_file, output_file)
