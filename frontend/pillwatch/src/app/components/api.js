
export async function fetchData(endpoint, options) {
    const response = await fetch(endpoint, options);
    const data = await response.json();
    return data;
  }

export async function loginUser(userame, password) {
      const data = {
          username: "username",
          password: "password",
        };
      try {
          const response = await fetch("http://127.0.0.1:5000/api/register", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
          });
          console.log(response.json);
          if (response.ok) {
            // Registration was successful
            // You can redirect to a different page or show a success message
          } else {
            // Handle registration errors, such as duplicate username or invalid password
            // You can display an error message to the user
          }
        } catch (error) {
          console.error("Error during registration:", error);
        }
    }
    const message = "hi";// loginUser();