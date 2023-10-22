import { DashboardLayout } from "./_layouts/DashboardLayout";
import { useUser } from "../queries";

export const IndexPage = () => {
  const { data: self, status: selfStatus } = useUser("me");

  return (
    <DashboardLayout statusArr={[selfStatus]}>
      {self && (
        <>
          <h1>Hello {self.username}!</h1>
          <a href="/auth/logout">Logout</a>
        </>
      )}
    </DashboardLayout>
  );
};
