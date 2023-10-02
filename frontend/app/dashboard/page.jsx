"use client";
import { useEffect, useState } from "react";
import axios from "axios";
export default function Main() {
  const [log, setLog] = useState("");
  const [base64, setBase64] = useState("");
  useEffect(() => {
    axios
      .post("http://52.72.1.74:8000/validate_token", {
        token: localStorage.getItem("token"),
        username: localStorage.getItem("username"),
      })
      .then((res) => {
        console.log(res.data.message);
        setLog(res.data.message);
      });
    axios.get("http://52.72.1.74:8000/graph").then((res) => {
      console.log(res.data.message);
      setBase64(res.data.message);
    });
  }, []);
  if (log == "") {
    return <p>loading ...</p>;
  }
  if (log == "valid token") {
    return (
      <div>
        <img src={`data:image/jpeg;base64,${base64}`} />
      </div>
    );
  } else {
    window.location.href = "/login";
  }
}
