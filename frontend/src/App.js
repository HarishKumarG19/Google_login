import React from 'react';
import { GoogleLogin } from '@react-oauth/google';
import axios from 'axios';

function App() {
    const responseMessage = (response) => {
        console.log(response);
        // You can send the token to your backend here
        axios.post('http://localhost:8000/google/login/', {
            token: response.credential,
        })
        .then(res => {
            console.log('Login Success:', res.data);
            // Handle successful login logic here
        })
        .catch(error => {
            console.error('Login Error:', error);
        });
    };

    return (
        <div className="App">
            <h2>React Google Sign-In</h2>
            <GoogleLogin
                onSuccess={responseMessage}
                onError={() => console.log('Login Failed')}
            />
        </div>
    );
}

export default App;
