let ENV = {
    API_BASE_URL: `http://0.0.0.0:5000`
}

if (process.env.NODE_ENV === 'production') {
    ENV = {
        API_BASE_URL: `${window.location.protocol}//${window.location.host}`
    }
}

export const { API_BASE_URL } = ENV