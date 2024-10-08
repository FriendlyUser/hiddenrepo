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
  { id: 1, bookName: "Book 1", bookDesc: "AbcdEfgh", code: "1234", time: "04-12-2020" },
  { id: 2, bookName: "Book 2", bookDesc: "AbcdEfgh", code: "1234", time: "04-12-2020" },
  { id: 3, bookName: "Book 3", bookDesc: "AbcdEfgh", code: "1234", time: "04-12-2020" },
  { id: 4, bookName: "Book 4", bookDesc: "AbcdEfgh", code: "1234", time: "04-12-2020" },
  { id: 5, bookName: "Book 5", bookDesc: "AbcdEfgh", code: "1234", time: "04-12-2020" },
];

const App = () => {
  const [dummyData] = useState(initialDummyData);

  return (
    <div className="App">
      <main>
        <Switch>
          <Route
            path="/dashboard"
            render={(props) => <MainBody {...props} data={dummyData} />}
            exact
          />
          <Route path="/" component={Login} exact />
          <Route path="/books/:id" component={BookDetails} />
        </Switch>
      </main>
    </div>
  );
};

const NavbarComponent = () => (
  <div>
    <Navbar bg="transparent" expand="lg">
      <Navbar.Brand>
        <img src="logo.png" alt="" className="nav-logo" />
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="ml-auto">
          <div className="account-info" type="button">
            <svg
              width="1.5em"
              height="1.5em"
              viewBox="0 0 16 16"
              className="bi bi-person-circle"
              fill="currentColor"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M13.468 12.37C12.758 11.226 11.195 10 8 10s-4.757 1.225-5.468 2.37A6.987 6.987 0 0 0 8 15a6.987 6.987 0 0 0 5.468-2.63z" />
              <path
                fillRule="evenodd"
                d="M8 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"
              />
              <path
                fillRule="evenodd"
                d="M8 1a7 7 0 1 0 0 14A7 7 0 0 0 8 1zM0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8z"
              />
            </svg>
          </div>
          <Link to="/">
            <Button variant="outline-danger">Logout</Button>
          </Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  </div>
);

const Book = ({ data }) => (
  <div className="book">
    <Link to={`/books/${ data.id }`}>
      <Card style={{ width: "100%" }}>
        <Card.Body>
          <Card.Title>{data.bookName}</Card.Title>
          <div className="overlay">
            <div className="view">View</div>
          </div>
        </Card.Body>
      </Card>
    </Link>
  </div>
);

const BookList = (props) => (
  <div className="container">
    <div className="row">
      {props.data.map((book) => (
        <div className="col-md-4" key={book.id}>
          <Book data={book} />
        </div>
      ))}
    </div>
  </div>
);

const Login = () => (
  <MDBContainer>
    <MDBRow className="login-container">
      <MDBCol md="5" className="l-col">
        <form>
          <p className="h5 text-center mb-4 l-title">Sign In</p>
          <div className="grey-text">
            <MDBInput label="Type your email" icon="envelope" group type="email" validate error="wrong" success="right" />
            <MDBInput label="Type your password" icon="lock" group type="password" validate />
          </div>
          <div className="text-center">
            <Link to="/dashboard"><MDBBtn color="indigo">Login</MDBBtn></Link>
          </div>
        </form>
      </MDBCol>
    </MDBRow>
  </MDBContainer>
);

const MainBody = (props) => (
  <div>
    <NavbarComponent />
    <div className="body-content">
      <div className="body-wrap">
        <Body data={props.data} />
      </div>
    </div>
  </div>
);

const BookDetails = ({ match }) => (
  <div>
    {match.params.id}
  </div>
);

const Body = (props) => {
  const [author] = useState("Author");

  return (
    <div className="welcome-wrap">
      <div className="w-title">Welcome, {author}</div>
      <div className="w-desc">Your Book List</div>
      <BookList data={props.data} />
    </div>
  );
};

const main = () => {
  ReactDOM.render(
    <BrowserRouter>
      <App />
    </BrowserRouter>,
    document.getElementById("root")
  );
};

main();
