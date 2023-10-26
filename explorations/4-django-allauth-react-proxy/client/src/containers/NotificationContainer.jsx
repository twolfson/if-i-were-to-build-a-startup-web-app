import { ToastContainer, toast } from "react-toastify";
import { useEffect } from "react";
import { useInvalidateMessages, useMessages } from "../queries";
import "react-toastify/dist/ReactToastify.css";

export const NotificationContainer = () => {
  const { error: messagesError, data: messagesData } = useMessages();
  const invalidateMessages = useInvalidateMessages();

  useEffect(() => {
    if (messagesError) {
      throw messagesError;
    }
    if (messagesData) {
      messagesData.messages.forEach((message) => {
        toast(message.message, { type: message.level_tag });
      });
      invalidateMessages();
    }
  }, [messagesError, messagesData, invalidateMessages]);

  return <ToastContainer position="top-center" />;
};
