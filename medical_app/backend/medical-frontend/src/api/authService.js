import API from "./api";


export const loginUser = async (userData) => {
  try {
    const response = await API.post("login/", {
      username: userData.username || "",  // Allow username or email
      email: userData.email || "",
      password: userData.password,
    });

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
