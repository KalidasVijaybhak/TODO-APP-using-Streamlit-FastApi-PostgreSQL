from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal, database
from datetime import datetime
from contextlib import asynccontextmanager

# Database models
class EntryDB(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date = Column(Date)

class CompletedEntryDB(Base):
    __tablename__ = "completed_entries"
    id = Column(Integer,primary_key=True,  index=True)
    name = Column(String, index=True)
    date = Column(Date)
        

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class Entry(BaseModel):
    name: str
    date: str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

@app.post("/add_entry")
async def add_entry(entry: Entry, db: Session = Depends(get_db)):
    new_entry = EntryDB(name=entry.name, date=entry.date)
    db.add(new_entry)
    db.commit()
    return {"message": "Entry added successfully"}

@app.post("/complete_entry/{index}")
async def complete_entry(index: int, db: Session = Depends(get_db)):
    entry = db.query(EntryDB).filter(EntryDB.id == index).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    
    completed_entry = CompletedEntryDB(
        
        name=entry.name,
        date=entry.date,
        
    )
    db.add(completed_entry)
    db.delete(entry)
    db.commit()
    return {"message": "Entry moved to completed"}

@app.get("/get_completed_entries")
async def get_completed_entries(db: Session = Depends(get_db)):
    entries = db.query(CompletedEntryDB).all()
    return entries

@app.get("/get_entries")
async def get_entries(db: Session = Depends(get_db)):
    entries = db.query(EntryDB).all()
    return entries

@app.delete("/delete_entry/{index}")
async def delete_entry(index: int, db: Session = Depends(get_db)):
    entry = db.query(EntryDB).filter(EntryDB.id == index).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    db.delete(entry)
    db.commit()
    return {"message": "Entry deleted successfully"}

@app.delete("/delete_completed_entry/{index}")
async def delete_completed_entry(index: int, db: Session = Depends(get_db)):
    entry = db.query(CompletedEntryDB).filter(CompletedEntryDB.id == index).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Completed entry not found")
    db.delete(entry)
    db.commit()
    return {"message": "Completed entry deleted successfully"}

@app.delete("/clear_entries")
async def clear_entries(db: Session = Depends(get_db)):
    db.query(EntryDB).delete()
    db.commit()
    return {"message": "All entries cleared"}

@app.delete("/clear_completed_entries")
async def clear_completed_entries(db: Session = Depends(get_db)):
    db.query(CompletedEntryDB).delete()
    db.commit()
    return {"message": "All completed entries cleared"}