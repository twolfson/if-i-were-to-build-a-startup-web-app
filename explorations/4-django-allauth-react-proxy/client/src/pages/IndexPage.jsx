import { BaseLayout } from "./_layouts/BaseLayout";
import { useUser } from "../queries";

export const IndexPage = () => {
  const { data: self, status: selfStatus } = useUser("me");

  return (
    <BaseLayout statusArr={[selfStatus]}>
      <h1>Hello {self.username}!</h1>
      <a href="/auth/logout">Logout</a>
    </BaseLayout>
  );
};
