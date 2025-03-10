import API from "./axiosConfig"; // Import the axios instance

export const registerUser = async (userData) => {
    try {
        const response = await API.post("register/", userData);
        return response.data; // Return the response data
    } catch (error) {
        console.error("Error registering user:", error.response?.data || error.message);
        throw new Error(error.response?.data?.detail || "Registration failed");
    }
};
export const loginUser = async (userData) => {
  try {
      const response = await API.post("login/", userData);
      localStorage.setItem("token", response.data.access); // Save JWT token
      return response.data;
  } catch (error) {
      console.error("Error logging in:", error.response?.data || error.message);
      throw new Error(error.response?.data?.detail || "Login failed");
  }
};
