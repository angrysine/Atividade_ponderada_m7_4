"use client";
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";

let handleLogin = () => {
  let username = document.getElementById("username").value;
  let password = document.getElementById("password").value;
  console.log(username, password);
  axios
    .post("http://127.0.0.1:8000/login", {
      username: username,
      password: password,
    })
    .then((response) => {
      console.log(response);
      window.localStorage.setItem("token", response.data.token);
      window.localStorage.setItem("username", username);
      toast.success("Register success");
      window.location.href = "/dashboard";
    })
    .catch((error) => {
      console.log(error);
      toast.error("Register failed");
    });
};

export default function RegisterPage() {
  return (
    <div className="h-screen bg-black flex justify-center items-center w-full">
      <div className="bg-white px-10 py-8 rounded-xl w-screen shadow-md max-w-sm">
        <div className="space-y-4">
          <h1 className="text-center text-2xl font-semibold text-gray-600">
            Register
          </h1>
          <div>
            <label
              htmlFor="email"
              className="block mb-1 text-gray-600 font-semibold"
            >
              User/Email
            </label>
            <input
              type="text"
              className="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full"
              id="username"
            />
          </div>
          <div>
            <label
              htmlFor="email"
              className="block mb-1 text-gray-600 font-semibold"
            >
              Password
            </label>
            <input
              type="text"
              className="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full"
              id="password"
            />
          </div>
        </div>
        <button
          className="mt-4 w-full bg-black text-indigo-100 py-2 rounded-md text-lg tracking-wide"
          onClick={handleLogin}
        >
          Login
        </button>
      </div>
    </div>
  );
}
