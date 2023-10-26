import { useQuery } from "@tanstack/react-query";
const e = encodeURIComponent;

export const useMessages = (options) => {
  return useQuery(
    ["messages"],
    () =>
      fetch("/auth/messages/").then((res) => res.json()),
    options
  );
};

export const useUser = (id, options) => {
  return useQuery(
    ["users", id],
    () =>
      fetch(`/api/users/${e(id)}`).then((res) => res.json()),
    options
  );
};
