"use client";
import { useState } from "react";
import { Form, Button } from "react-bootstrap";
import {loginUser} from './api';

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  // const handleSubmit = (e) => {
  //   console.log(username, password);
  //   setUsername("jldskfj");

  //   e.preventDefault();
  //   // Create a data object to send to the server
  //   const data = {
  //     username: username,
  //     password: password,
  //   };

  //   try {
  //     const response = await fetch("http://127.0.0.1:5000/api/register", {
  //       method: "POST",
  //       headers: {
  //         "Content-Type": "application/json",
  //       },
  //       body: JSON.stringify(data),
  //     });
  //     console.log(response.json);
  //     if (response.ok) {
  //       // Registration was successful
  //       // You can redirect to a different page or show a success message
  //     } else {
  //       // Handle registration errors, such as duplicate username or invalid password
  //       // You can display an error message to the user
  //     }
  //   } catch (error) {
  //     console.error("Error during registration:", error);
  //   }
  // };

  const onClick = (e) => {
    loginUser(username, password);
  };

  return (
    <div>
        {/* {message} */}
      <Form onSubmit={onClick}>
        <Form.Label>Username</Form.Label>
        <Form.Control
          id="form-id"
          type="username"
          placeholder="Enter username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <Form.Label>Password</Form.Label>
        <Form.Control
          id="form-password"
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <Button variant="primary" type="submit">
          Register
        </Button>
      </Form>
    </div>
  );
}
