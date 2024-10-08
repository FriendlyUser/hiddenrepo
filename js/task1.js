```javascript
import React, { useState } from "react";
import ReactDOM from "react-dom";
import '@fortawesome/fontawesome-free/css/all.min.css';
import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbreact/dist/css/mdb.css';
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter, Route, Switch, Link } from "react-router-dom";
import { Card, Navbar, Nav, Button } from "react-bootstrap";
import { MDBContainer, MDBRow, MDBCol, MDBInput, MDBBtn } from 'mdbreact';

// Dummy data used by the App component
const initialDummyData = [
  { id: 1, bookName: "The Hitchhiker's Guide to the Galaxy", bookDesc: "A comedic science fiction series", code: "4242", time: new Date(2023, 4, 10) },
  { id: 2, bookName: "Pride and Prejudice", bookDesc: "A classic romance novel", code: "1813", time: new Date(2023, 0, 28) },
  { id: 3, bookName: "The Lord of the Rings", bookDesc: "A high fantasy epic", code: "0001", time: new Date(2023, 6, 29) },
  { id: 4, bookName: "To Kill a Mockingbird", bookDesc: "A novel about racial injustice", code: "1960", time: new Date(2023, 2, 15) },
  { id: 5, bookName: "1984", bookDesc: "A dystopian social science fiction novel", code: "9849", time: new Date(2023, 5, 8) },
];

// ... (App, NavbarComponent, BookList, Login, MainBody, BookDetails remain the same)

const Book = ({ data }) => (
  <div className="book">
    <Link to={`/books/${data.id}`}>
      <Card style={{ width: "100%" }}>
        <Card.Body>
          <Card.Title>{data.bookName}</Card.Title>
          <Card.Text>{data.bookDesc}</Card.Text>
          <Card.Text>Code: {data.code}</Card.Text>
          <Card.Text>Added: {formatDate(data.time)}</Card.Text> {/* Display the time */}
          <div className="overlay">
            <div className="view">View</div>
          </div>
        </Card.Body>
      </Card>
    </Link>
  </div>
);

// Helper function to format date as YYYY-MM-DD
const formatDate = (date) => {
  const year = date.getFullYear();
  const month = ('0' + (date.getMonth() + 1)).slice(-2); // Add leading zero if needed
  const day = ('0' + date.getDate()).slice(-2); // Add leading zero if needed
  return `${year}-${month}-${day}`;
};


const Body = (props) => {
  // ... (rest of the Body component remains the same)
};

const main = () => {
  // ... (rest of the main function remains the same)
};

main();
```

Here's the breakdown of the changes:

- **`formatDate` function:**
  - This function now directly formats the date as YYYY-MM-DD.
  - It uses `getFullYear`, `getMonth` (adding 1 to get the correct month), and `getDate`.
  - Leading zeros are added to the month and day if needed using `('0' + ...).slice(-2)`.
- **`Book` component:**
  - We're calling `formatDate(data.time)` to display the time in the desired format.

Now the "Added" date will be displayed as "YYYY-MM-DD". 
