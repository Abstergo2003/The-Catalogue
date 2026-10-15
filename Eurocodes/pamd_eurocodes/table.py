from typing import List, Any

class Table():
    def __init__(self, headers: List[str], values: List[List[Any]], caption: str, footnote: str):
        self.headers = headers
        self.values = values
        self.caption = caption
        self.footnote = footnote
    
    def __repr__(self):
        headers_string = "|"
        breaker_line = "|"
    
        for i in self.headers:
            headers_string += f"{i}|"
            breaker_line += "-"*len(i)+"|"
    
        table_content = ""
        for i, row in enumerate(self.values):
            table_content += "|"
            
            for value in row:
                table_content += f"{value}|"
            
            table_content += "\n"
    
        caption_html = f"<span style='text-align: center; display: block; font-style: italic;'>{self.caption}</span>"
        return f"{caption_html} \n{headers_string}\n{breaker_line}\n{table_content}  {self.footnote}"

    def toDXF(self, filename: str, cell_width: float = 50.0, cell_height: float = 10.0):
        try:
            import ezdxf
        except ImportError:
            return f"*(Error: ezdxf library is not installed. Cannot generate {filename})*"
            
        doc = ezdxf.new('R2010')
        msp = doc.modelspace()
        
        # Construct full grid data
        rows = [self.headers] + self.values
        num_rows = len(self.rows)
        num_cols = len(self.headers)
        
        # Draw horizontal grid lines
        for i in range(num_rows + 1):
            y = -i * cell_height
            msp.add_line((0, y), (num_cols * cell_width, y))
            
        # Draw vertical grid lines
        for j in range(num_cols + 1):
            x = j * cell_width
            msp.add_line((x, 0), (x, -num_rows * cell_height))
            
        # Draw text centered in each cell
        for i, row in enumerate(rows):
            y = -i * cell_height - (cell_height / 2)
            for j, cell_val in enumerate(row):
                if j >= num_cols: continue # Safety bounds
                x = j * cell_width + (cell_width / 2)
                msp.add_text(
                    str(cell_val),
                    dxfattribs={
                        'height': cell_height * 0.4,
                    }
                ).set_placement((x, y), align=ezdxf.enums.TextEntityAlignment.MIDDLE_CENTER)
                
        doc.saveas(filename)
        return f"*[Successfully exported table to {filename}]({filename})*"

    def get(self, query = None, rowNumber = None, valueID = None):
        if query is None and rowNumber is None and valueID is None:
            return "Pass at leats one specifier"

        selected = None

        if query is not None:
            for val in self.values:
                print(val)
                if query in val:
                    selected = val

        if rowNumber is not None:
            selected = self.values[rowNumber-1]

        if valueID is not None:
            index = self.headers.index(valueID)
            return f"{selected[index]}"

        string = ""
        for i in selected:
            string += f"{i} - "
        return string[:-3]
