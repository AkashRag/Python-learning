from fastapi import FastAPI
from pydantic import BaseModel
class Note(BaseModel):
    id: int
    title: str
    content: str
    done: bool

notes= [ { "id": 1, "title": "Chapter 1", "content": "How to call API",  "done": False }, 
        { "id": 2, "title": "Chapter 2", "content": "How to make validation", "done":False }]
app = FastAPI()
@app.get("/notes")
def get_notes():
    return notes
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note
    return {"message": "Note not found"}
@app.post("/notes")
def create_note(note: Note):
    notes.append(note)
    return {"message": f"{note.title} created successfully", "note": note}

@app.patch("/notes/{note_id}")
def note_update(note_id: int, note: Note):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = note.title
            note["content"] = note.content
            note["done"] = note.done
            return {"message": f"{note.title} updated successfully", "note": note}
        
    return {"message": "Note not found"}
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return {"message": f"{note.title} is deleted successflly"}
    return {"message":"Note not found "}



