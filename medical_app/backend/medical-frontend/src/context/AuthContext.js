import { createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import jwtDecode from "jwt-decode";
import API from "../api/api";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  // Check for existing token on app start
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      try {
        const decodedUser = jwtDecode(token);
        setUser(decodedUser);
      } catch (error) {
        console.error("Invalid token:", error);
        logout();
      }
    }
    setLoading(false);
  }, []);

  // Login function
  const login = async (credentials) => {
    try {
      const response = await API.post("login/", credentials);
      const { access } = response.data;
      localStorage.setItem("token", access);
      const decodedUser = jwtDecode(access);
      setUser(decodedUser);
      navigate("/dashboard");
    } catch (error) {
      console.error("Login failed:", error.response?.data);
    }
  };

  // Register function
  const register = async (userData) => {
    try {
      await API.post("register/", userData);
      navigate("/login");
    } catch (error) {
      console.error("Registration failed:", error.response?.data);
    }
  };

  // Logout function
  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
    navigate("/login");
  };

  return (
    <AuthContext.Provider value={{ user, login, register, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};
