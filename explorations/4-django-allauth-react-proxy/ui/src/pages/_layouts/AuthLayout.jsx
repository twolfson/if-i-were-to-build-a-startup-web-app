import { BaseLayout } from "./BaseLayout";

// Based on: explorations/2-django-allauth/app/templates/_layouts/auth.html
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
