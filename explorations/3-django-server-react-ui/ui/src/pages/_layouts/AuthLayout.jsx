import { BaseLayout } from "./BaseLayout";

// Based on: explorations/2-django-allauth/app/templates/_layouts/auth.html
// TODO: Handle `messages` like https://github.com/twolfson/if-i-were-to-build-a-startup-web-app/blob/acf34e2f52204084300383ba029b68b0c838af99/explorations/2-django-allauth/app/templates/_layouts/auth.html#L11-L19
export const AuthLayout = ({ children }) => {
  return (
    <BaseLayout>
      <div className="bg-light vh-100">
        <div className="container pt-5">
          <div className="p-3 w-100 mx-auto card" style={{ maxWidth: "480px" }}>
            <div className="card-body p-0">{children}</div>
          </div>
        </div>
      </div>
    </BaseLayout>
  );
};
