# Use official Node.js Alpine image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Install dependencies first (caching layer)
COPY package.json package-lock.json ./
RUN npm ci

# Copy the rest of the application
COPY . .

# Build the Next.js application
RUN npm run build

# Set environment variables
ENV PORT=3000
ENV NODE_ENV=production

# Expose port
EXPOSE 3000

# Start the application
CMD ["npm", "start"]
