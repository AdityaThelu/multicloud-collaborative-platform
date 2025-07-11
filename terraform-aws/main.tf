resource "aws_s3_bucket" "multicloud_bucket" {
  bucket = "my-multicloud-bucket"
  acl    = "private"
}
