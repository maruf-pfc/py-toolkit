import os
import typer
from pathlib import Path
from typing import Optional, List
from PIL import Image
import customtkinter as ctkinter
from tkinterdnd2 import TkinterDnD, DND_FILES

# Set appearance mode and color theme
ctkinter.set_appearance_mode("dark")
ctkinter.set_default_color_theme("blue")

app = typer.Typer(help="🎨 Graphics utilities and image processing.")

COMMAND_NAME = "graphics"

class GraphicsResizerApp(ctkinter.CTk, TkinterDnD.DnDWrapper):
    def __init__(self):
        super().__init__()
        # Initialize DnD correctly
        self.TkdndVersion = TkinterDnD._require(self)
        
        self.title("PyToolkit - Image Resizer")
        self.geometry("600x500")
        
        # Data
        self.selected_files: List[Path] = []
        
        # Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # Title
        self.label = ctkinter.CTkLabel(self, text="🖼️ Image Resizer", font=ctkinter.CTkFont(size=24, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Drop Zone
        self.drop_frame = ctkinter.CTkFrame(self, border_width=2, border_color="#3B8ED0", corner_radius=10)
        self.drop_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.drop_frame.grid_columnconfigure(0, weight=1)
        self.drop_frame.grid_rowconfigure(0, weight=1)
        
        self.drop_label = ctkinter.CTkLabel(
            self.drop_frame, 
            text="Drag & Drop Images or Folders Here\n(or click to select)", 
            font=ctkinter.CTkFont(size=14)
        )
        self.drop_label.grid(row=0, column=0, padx=20, pady=40)
        
        # DnD Binding
        self.drop_frame.drop_target_register(DND_FILES)
        self.drop_frame.dnd_bind('<<Drop>>', self.handle_drop)
        
        # Controls Frame
        self.controls_frame = ctkinter.CTkFrame(self)
        self.controls_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.controls_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        self.width_entry = ctkinter.CTkEntry(self.controls_frame, placeholder_text="Width (px)")
        self.width_entry.grid(row=0, column=0, padx=10, pady=10)
        
        self.height_entry = ctkinter.CTkEntry(self.controls_frame, placeholder_text="Height (px)")
        self.height_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.aspect_checkbox = ctkinter.CTkCheckBox(self.controls_frame, text="Maintain Aspect", variable=ctkinter.BooleanVar(value=True))
        self.aspect_checkbox.grid(row=0, column=2, padx=10, pady=10)
        
        # Status/Log
        self.log_box = ctkinter.CTkTextbox(self, height=150)
        self.log_box.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
        self.log_box.insert("0.0", "Ready to resize...\n")
        self.log_box.configure(state="disabled")

        # Action Button
        self.resize_button = ctkinter.CTkButton(self, text="Resize Now", command=self.start_resize, state="disabled")
        self.resize_button.grid(row=4, column=0, padx=20, pady=(10, 20))

        # Progress Bar
        self.progress_bar = ctkinter.CTkProgressBar(self)
        self.progress_bar.grid(row=5, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.progress_bar.set(0)

    def log(self, message: str):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", f"{message}\n")
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def handle_drop(self, event):
        files = self.parse_drop_files(event.data)
        valid_files = []
        extensions = (".jpg", ".jpeg", ".png", ".webp", ".bmp")
        
        for f in files:
            path = Path(f)
            if path.is_file() and path.suffix.lower() in extensions:
                valid_files.append(path)
            elif path.is_dir():
                for subf in path.iterdir():
                    if subf.is_file() and subf.suffix.lower() in extensions:
                        valid_files.append(subf)
        
        if valid_files:
            self.selected_files = valid_files
            self.log(f"Added {len(valid_files)} images.")
            self.drop_label.configure(text=f"{len(valid_files)} images selected")
            self.resize_button.configure(state="normal")
        else:
            self.log("Error: No valid image files dropped.")

    def parse_drop_files(self, data: str) -> List[str]:
        # TkinterDnD data can be curly-braced or space-separated
        import re
        if data.startswith('{'):
            return re.findall(r'\{(.*?)\}', data)
        return data.split()

    def start_resize(self):
        width_str = self.width_entry.get()
        height_str = self.height_entry.get()
        
        if not width_str and not height_str:
            self.log("Error: Enter width or height.")
            return

        try:
            width = int(width_str) if width_str else None
            height = int(height_str) if height_str else None
        except ValueError:
            self.log("Error: Invalid width/height value.")
            return

        self.resize_button.configure(state="disabled")
        self.progress_bar.set(0)
        
        maintain_aspect = self.aspect_checkbox.get()
        
        total = len(self.selected_files)
        success_count = 0
        
        for i, input_path in enumerate(self.selected_files):
            output_path = input_path.parent / f"resized_{input_path.name}"
            success, msg = self.resize_image_logic(input_path, output_path, width, height, maintain_aspect)
            if success:
                success_count += 1
            self.log(f"{'✅' if success else '❌'} {input_path.name}: {msg}")
            self.progress_bar.set((i + 1) / total)
            self.update_idletasks()
            
        self.log(f"\nFinished! {success_count}/{total} images resized.")
        self.resize_button.configure(state="normal")

    def resize_image_logic(self, input_path: Path, output_path: Path, width: Optional[int], height: Optional[int], maintain_aspect: bool):
        try:
            with Image.open(input_path) as img:
                original_width, original_height = img.size
                
                if width and height:
                    new_size = (width, height)
                elif width:
                    if maintain_aspect:
                        h = int((width / original_width) * original_height)
                    else:
                        h = original_height
                    new_size = (width, h)
                elif height:
                    if maintain_aspect:
                        w = int((height / original_height) * original_width)
                    else:
                        w = original_width
                    new_size = (w, height)
                else:
                    return False, "No size specified"

                img = img.convert("RGBA") if img.mode in ("P", "RGBA") else img.convert("RGB")
                resample = getattr(Image, "Resampling", Image).LANCZOS
                resized_img = img.resize(new_size, resample)
                resized_img.save(output_path)
                return True, f"{new_size[0]}x{new_size[1]}"
        except Exception as e:
            return False, str(e)

@app.callback(invoke_without_command=True)
def launch_gui(ctx: typer.Context):
    """
    Launch the GUI Image Resizer.
    """
    if ctx.invoked_subcommand is not None:
        return
    app_gui = GraphicsResizerApp()
    app_gui.mainloop()

if __name__ == "__main__":
    app()
