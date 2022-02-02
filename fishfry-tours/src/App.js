import './App.css';
import PageHeader from './PageHeader';
import PageFooter from './PageFooter';
import Dropzone from './Dropzone';
import React from 'react';
import BoatCardList from './BoatCardList';
import { DragDropContext, Draggable, Droppable } from "react-beautiful-dnd"
import { Button, Grid, TextField } from '@material-ui/core';
import { API_BASE_URL } from './env';

const axios = require('axios').default

class App extends React.Component {
  constructor() {
    super()
    this.state = {
      boats: [],
      newBoatName: ''
    }
    this.axios_instance = axios.create({
      baseURL: API_BASE_URL,
      config: {
        headers: {
          post: {
          "Access-Control-Allow-Origin": "*"
          }
        }
      }
    })
  }

  componentDidMount() {
    this.getBoats()
  }

  getBoats() {
    const queryString = `query { boats { id name status }}`
    this.axios_instance.post('/graphql', {query: queryString}).then((response) => {
      this.setState( {
        boats: response.data.data.boats
      })
    })
  }

  addBoat(boatName) {
    if(boatName.length > 0) {
      const mutationString = `mutation { boats { addBoat(name: "${boatName}") {id name status } }}`
      this.axios_instance.post('graphql', {query: mutationString}).then((response) => {
        if (response.status === 200) {
          this.getBoats()
          this.setState({
            newBoatName: ''
          })
        }
      })
    }
  }
  
  deleteBoat = (boatId) => {
    const mutationString = `mutation { boats { deleteBoat(id: ${boatId}) }}`
    this.axios_instance.post('graphql', {query: mutationString}).then((response) => {
      console.log(response)
      if (response.status === 200 && response.data.data.boats.deleteBoat === true) {
        this.getBoats()
      }
    })
  }

  updateBoatStatus(boatId, newStatus) {
    const mutationString = `mutation { boats { updateBoatStatus(id: ${boatId}, status: ${newStatus}) { id name status }}}`
    this.axios_instance.post('graphql', {query: mutationString}).then(function(response) {
      console.log(response)
    })
  }

  onDrop = (acceptedFiles) => {
    console.log(acceptedFiles)
  }

  reorder = (list, startIndex, endIndex) => {
    const result = Array.from(list)
    const [removed] = result.splice(startIndex, 1)
    result.splice(endIndex, 0, removed)

    return result
  }

  onDragEnd = (result) => {
    // if dropped outside list
    if (!result.destination) {
      return;
    }
    const items = this.reorder(this.state.boats, result.source.index, result.destination.index)

    this.setState({boats: items})
  }

  grid = 8

  getItemStyle = (isDragging, draggableStyle) => ({
    userSelect: "none",
    padding: this.grid * 2,
    margin: `0 0 ${this.grid}px 0`,

    background: isDragging ? "lightgreen" : "grey",
    ...draggableStyle
  })

  getListStyle = isDraggingOver => ({
    background: isDraggingOver ? "lightblue" : "lightgrey",
    padding: Grid,
    width: 250
  })



  render() {
    return (
      <div className="App">
        <PageHeader />
        <h1 className='text-center'>Drag and Drop example</h1>
        <Dropzone onDrop={this.onDrop} />
        {/* <DragDropContext onDragEnd={onDragEnd}>
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
        </DragDropContext> */}
        <TextField variant="outlined" label="Boat Name" size="small" onChange={(e) => {
          this.setState({newBoatName: e.target.value})
        }} />
        <Button variant="contained" onClick={() => {this.addBoat(this.state.newBoatName)}}>
          Add Boat
        </Button>
        <BoatCardList boatCards={this.state.boats} deleteBoat={this.deleteBoat} />
        <PageFooter />
      </div>
    );
  }
  
}

export default App
