import { useEffect } from "react";
export default function Main() {
    useEffect(() => {
        window.location.href = "/dashboard";
    }, []);
}