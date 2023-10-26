import { ToastContainer, toast } from "react-toastify";
import { useEffect } from "react";
import { useMessages } from "../queries";
import "react-toastify/dist/ReactToastify.css";

export const NotificationContainer = () => {
  const { error: messagesError, data: messagesData } = useMessages();

  useEffect(() => {
    if (messagesError) {
      throw messagesError;
    }
    if (messagesData) {
      messagesData.messages.forEach((message) => {
        toast(message.message, { type: message.level_tag });
      });
    }
  }, [messagesError, messagesData]);

  return <ToastContainer position="top-center" />;
};
