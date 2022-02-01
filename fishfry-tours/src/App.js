import './App.css';
import PageHeader from './PageHeader';
import PageFooter from './PageFooter';
import Dropzone from './Dropzone';
import { useCallback, useState } from 'react';
import BoatCardList from './BoatCardList';
import { DragDropContext, Draggable, Droppable } from "react-beautiful-dnd"
import { Grid } from '@material-ui/core';


function App() {
  const [boats, setBoats] = useState([])

  const onDrop = useCallback(acceptedFiles => {
    console.log(acceptedFiles)
  }, [])

  const grid = 8

  const getItemStyle = (isDragging, draggableStyle) => ({
    userSelect: "none",
    padding: grid * 2,
    margin: `0 0 ${grid}px 0`,

    background: isDragging ? "lightgreen" : "grey",
    ...draggableStyle
  })

  const getListStyle = isDraggingOver => ({
    background: isDraggingOver ? "lightblue" : "lightgrey",
    padding: Grid,
    width: 250
  })

  return (
    <div className="App">
      <PageHeader />
      <h1 className='text-center'>Drag and Drop example</h1>
      <Dropzone onDrop={onDrop} />
      <DragDropContext onDragEnd={}>
        <Droppable droppableId='droppable'>
          {(provided, snapshot) => (
            <div {...provided.droppableProps} ref={provided.innerRef} style={getListStyle(snapshot.isDraggingOver)} >
              {this.state.items.map((item, index) => (
                <Draggable key={item.id} draggableId={item.id} index={index} >
                  {(provided, snapshot) => (
                    <div ref={provided.innerRef} {...provided.draggableProps} {...provided.dragHandleProps}
                    style={getItemStyle(snapshot.isDragging, provided.draggableProps.style)}
                    >
                      {item.content}
                    </div>
                  )}
                </Draggable>
              ))}
              {provided.placeholder}
            </div>
          )}

        </Droppable>
      </DragDropContext>
      <BoatCardList boatCards={boats} />
      <PageFooter />
    </div>
  );
}

export default App;
