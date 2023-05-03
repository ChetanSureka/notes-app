import React, { useEffect, useState } from 'react'
// import notes from '../assets/data'
import ListItem from '../components/ListItem'
import AddButton from '../components/AddButton'

const NotesListPage = () => {
    const [notes, setNotes] = useState([])

    useEffect(() => {
        getNotes()
    }, [])

    let getNotes = async() => {
        let reponse = await fetch("/api/notes/")
        let data = await reponse.json()
        console.log(data)
        setNotes(data)
    }

    return (
        <>
            <div className="notes">
                <div className='notes-header'>
                    <h2 className='notes-title'>&#9782; Notes</h2>
                    <p>{notes.length}</p>
                </div>
                <div className='notes-list'>
                    {notes.map(note => (
                        <ListItem key={note.id} note={note} />
                    ))}
                </div>
                <AddButton />
            </div>
        </>
    )
}

export default NotesListPage