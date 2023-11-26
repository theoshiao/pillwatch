"use client";
import { useState } from "react";
import { Form, Button } from "react-bootstrap";
import { useRouter, usePathname} from 'next/navigation';

export default function Login() {
  const pathname = usePathname();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");


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
