import API from "./api";

export const loginUser = async (userData) => {
  try {
    const response = await API.post("login/", userData);
    
    if (response.data.access) {
      localStorage.setItem("token", response.data.access); 
      localStorage.setItem("refresh", response.data.refresh);
    }
    
    return response.data;
  } catch (error) {
    console.error("Login error:", error);
    throw error;
  }
};

export const logoutUser = () => {
  localStorage.removeItem("token");
  localStorage.removeItem("refresh");
  window.location.href = "/login"; // Redirect to login
};
